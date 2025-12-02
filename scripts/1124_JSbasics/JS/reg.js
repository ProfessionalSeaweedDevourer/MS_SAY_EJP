function register(){
    var nInput = document.getElementById("nameInput");
    var pInput = document.getElementById("priceInput");

    var n = nInput.value;
    var p = pInput.value;

    var queryString = "?productName=" + encodeURIComponent(n) + "&price=" + encodeURIComponent(p);

    // 3. result.html 페이지로 이동
    location.href = "result.html" + queryString;
}