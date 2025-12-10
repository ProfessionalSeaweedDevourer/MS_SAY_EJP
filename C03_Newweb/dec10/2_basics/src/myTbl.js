import React from "react";

// React의 Hook: '함수를 클래스처럼' 쓰기

const MyTbl = () => { // 클래스 역할의 함수

    // 멤버 변수와 메소드 만들기
    const [txt, setTxt] = useState("");
    // 멤버 변수 txt를 빈 값으로 선언
    // 메소드 setTxt 선언: txt 값 바꿀 때 활용

    const showwww = () => { // 메소드 역할의 함수
        alert("!!!");
    };

    const keyUpp = (e) => { // 이벤트 호출도 이렇게 할 수 있다. function(e)와 같다.
        // e.target : $(this)
        setTxt(e.target.value); // 키를 건드릴 '때마다' txt의 값을 상시 업데이트한다.
    }

  return (
    <table border = "1">
        <tr>
            <td>
                <input value={txt} />
            </td>
        </tr>
        <tr>
            <td>
                <button> 눌러욧 </button>
            </td>
        </tr>
    </table>
  )
}

export default MyTbl