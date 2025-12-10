function arrayTest(){
    var a = [234, 5, 67, 8910];

    alert(a.length); // 배열 길이 (내용물의 개수)
    alert(a[0]); // 0번 = 첫 번째 요소
    // alert(a[0:3]): // python에서만 가능

    for (var i = 0; i<a.length; i++){
        alert(a[i]);
    }
    
    for (var v of a){
        alert(v);
    }
    
}

function objTest(){
 // class를 쓰지 않고 구현하는 객체
    var d = {};
    alert(d);
    alert(d.name);
    
}

function arrayObjTest(){
    // var pups = [
        // 여러 객체 배열
}