import React from 'react'

const studentBBS = () => {
    const regStudent = () => { 
        axios
        .get(`http://localhost:9999/student.reg?name=${student.name}&age=${student.age}`)
        .then((res) => {
            sessionStorage.setItem("myJWT", res.data.EJPJWT);
            setStudent({name:"", age:""})
        })
     }

     const showStudent = ()  => {
        alert(sessionStorage.getItem("myJWT")) // sessionStorage: 세션 유지 시간 동안 존재하는 저장 공간. 시간 지난다고 값이 없어지지는 않는데 복호화를 못 하게 됨
     }

     const showStudent2 = () => {
        axios
            .get(
                `http://localhost:9999/student.get?jwt=${sessionStorage.getItem(
                    "myJWT"
                )}`
            )
            .then((res) => {
                alert(JSON.stringify(res.data))
            })
     }


  return (
    <>
        이름: {" "}
        <input value={student.name} name="name" onChange={changeStudent} />
        <br />
        나이: {" "}
        <input value={student.age} name="age" onChange={changeStudent} />
        <br />
        <button onClick={regStudent}> JWT 생성 </button>
        <button onClick={showStudent}> JWT 확인 </button>
        <button onClick={showStudent2}> JWT 복호화 </button>
        <button onClick={updateJWT}> JWT 갱신 </button>
        <button onClick={deleteJWT}> JWT 삭제 </button>
        <hr />

    </>
  )

}

export default studentBBS