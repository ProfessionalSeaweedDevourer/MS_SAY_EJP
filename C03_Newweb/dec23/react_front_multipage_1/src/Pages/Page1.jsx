import React from 'react'
import { Link } from 'react-router-dom'

const Page1 = () => {
  return (
    <>
      <h1> 페이지 1 </h1>
      <a href="/p2.go"> 페이지 2로 이동하기(a 태그 사용) </a>
      <br />
      <Link to="/p2.go"> 페이지 2로 이동하기(Link to 사용) </Link>
    </>
  )
}

export default Page1