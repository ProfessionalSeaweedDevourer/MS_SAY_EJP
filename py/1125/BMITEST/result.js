function getJudgment(bmi) {
    if (bmi > 120) {
        return "비만 😥";
    } else if (bmi >= 80 && bmi <= 120) {
        return "정상 😀";
    } else if (bmi < 80) {
        return "저체중 😟";
    } else {
        return "판정 오류";
    }
}

function calculateBMI(height, weight) {
    
    function stdWeightCalc(height){
        const stdWeight = (height - 100) * 0.9;
        return stdWeight; 
    }

    function getBMI(weight, stdWeight){
        const bmi = (weight / stdWeight) * 100;
        return bmi;
    }
    
    const stdWeightNumber = stdWeightCalc(height); 
    const BMINumber = getBMI(weight, stdWeightNumber);

    const judgmentResult = getJudgment(BMINumber);
    
    return {
        stdWeight: stdWeightNumber.toFixed(1),
        bmi: BMINumber.toFixed(1),
        judgment: judgmentResult
    };
}