function isEmpty(input){
    return !input.value.trim()
}

function isNotNum(input){
    // 숫자가 아니거나 공백이 있거나, 0 이하인 경우까지 포함하여 검증
    return isNaN(input.value) || (input.value.indexOf(" ") != -1) || (parseFloat(input.value) <= 0)
}

function notEqual(input1, input2){
    return input1.value != input2.value
}