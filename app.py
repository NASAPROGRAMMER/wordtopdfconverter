from flask import Flask, render_template, request, send_from_directory
import os
import subprocess
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
CONVERTED_FOLDER = "converted"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    file = request.files.get("file")
    conversion_type = request.form.get("conversionType")

    if not file or not conversion_type:
        return "Invalid request", 400

    filename = secure_filename(file.filename)
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(input_path)

    name, ext = os.path.splitext(filename)
    ext = ext.lower()

    if conversion_type == "doc-to-pdf" and ext in [".doc", ".docx"]:
        output_format = "pdf"
    else:
        return "Unsupported conversion or file type", 400

    try:
        subprocess.run([
            "libreoffice",
            "--headless",
            "--convert-to", output_format,
            "--outdir", CONVERTED_FOLDER,
            input_path
        ], check=True)

        output_filename = f"{name}.{output_format}"
        return send_from_directory(CONVERTED_FOLDER, output_filename, as_attachment=True)
    except subprocess.CalledProcessError as e:
        return f"Conversion failed. LibreOffice error: {str(e)}", 500
    except Exception as e:
        return f"Unexpected error: {str(e)}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
