function displayResults() {
    
    const params = new URLSearchParams(window.location.search);

    const name = params.get('name');
    const weight = params.get('weight');
    const stdWeight = params.get('stdWeight');
    const bmi = params.get('bmi');
    const judgment = params.get('judgment');
    const photoPath = params.get('photo_path');

    document.getElementById('resultName').textContent = name || 'N/A';
    document.getElementById('resultWeight').textContent = (weight || 'N/A') + ' kg';
    document.getElementById('resultStdWeight').textContent = (stdWeight || 'N/A') + ' kg';
    document.getElementById('resultBMI').textContent = (bmi || 'N/A') + ' %';
    document.getElementById('resultJudgment').textContent = judgment || 'N/A';
    
    if (judgment.includes("비만")) {
        document.getElementById('resultJudgment').style.fontWeight = 'bold';
        document.getElementById('resultJudgment').style.color = 'red';
    } else if (judgment.includes("정상")) {
        document.getElementById('resultJudgment').style.color = 'blue';
    }

    const photoArea = document.getElementById('photoArea');
    if (photoPath && photoPath !== 'null' && photoArea) {
        const serverOrigin = 'http://127.0.0.1:8000';
        const fullPhotoUrl = serverOrigin + photoPath;
        
        const imageElement = document.createElement('img');
        imageElement.src = fullPhotoUrl; 
        imageElement.alt = '업로드된 사용자 사진';
        imageElement.style.maxWidth = '100%'; 
        imageElement.style.marginTop = '20px';
        imageElement.style.border = '1px solid #ddd';
        photoArea.appendChild(imageElement);
    }
}