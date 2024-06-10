export default function FileCard() {
    async function uploadFile() {
        const formData = new FormData();
        const fileInput = document.getElementById("userFile");
        formData.append('file', fileInput.files[0]);
    
        response = await fetch("http://127.0.0.1:5000/upload", {
            method: "POST",
            body: formData,
        });
    
        if(!response.ok) {
            console.error('File upload error!');
        } else {
            const responseDataObject = await response.json();
            document.getElementById('fileUploadFeedback').innerHTML += '<p>File is uploaded successfully!</p>'
            console.log('File uploaded successfully', responseDataObject);
        }
    }

    return (
        <div className="card">
            <input type="file" />
            <button onClick={uploadFile}>
                Upload File
            </button>
          <div id="fileUploadFeedback"></div>
        </div>
    );
}