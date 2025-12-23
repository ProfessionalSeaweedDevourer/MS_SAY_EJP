import React from 'react'
import { useSearchParams } from 'react-router-dom'

const Page5 = () => {
    const [menu, setMenu] = useSearchParams(); // 요청 패러미터로 넘어오는 값을 menu에 담음
  return (
    <>
        <h1> 페이지 5 </h1>
        메뉴: {menu.get("name")}
        <br />
        가격: {menu.get("price")}
        <hr />
        <Link to="/p6.go?title=삼국지&price=10000"> 페이지 6으로 이동: 삼국지 10000 </Link>
        <br />
        <Link to="/p6.go?title=파이썬&price=20000"> 페이지 6으로 이동: 파이썬 20000 </Link>
        
    </>
  )
}

export default Page5