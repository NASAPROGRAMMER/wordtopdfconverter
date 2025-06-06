document.getElementById("uploadForm").addEventListener("submit", async function (e) {
  e.preventDefault();
  const formData = new FormData(this);
  // Add fixed conversion type
  formData.append("conversionType", "doc-to-pdf");

  try {
    const response = await fetch("/convert", {
      method: "POST",
      body: formData,
    });

    if (response.ok) {
      const blob = await response.blob();
      const contentDisposition = response.headers.get("Content-Disposition");
      const filename = contentDisposition?.split("filename=")[1] || "converted.pdf";

      const link = document.createElement("a");
      link.href = window.URL.createObjectURL(blob);
      link.download = filename.replaceAll('"', '');
      link.click();
    } else {
      const errText = await response.text();
      alert("Gagal mengkonversi file:\n" + errText);
    }
  } catch (err) {
    alert("Terjadi kesalahan saat mengirim request:\n" + err);
  }
});
