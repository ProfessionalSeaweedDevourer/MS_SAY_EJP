import React from 'react'
import { useParams } from 'react-router-dom'

const Page4 = () => {
    const student = useParams(); // 주소 꼴로 넘어오는 값을 student로 받음
  return (
    <>
        <h1> 페이지 4 </h1>
        이름: {student.name}
        <br />
        나이: {student.age}
        <hr />
        <Link to = "/p5.go"> 페이지 5로 이동 </Link>
    </>
  )
}

export default Page4