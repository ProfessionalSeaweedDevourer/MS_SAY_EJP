import React from 'react'
import { useSearchParams } from 'react-router-dom'

const Page6 = () => {
    const [bookdata, setBookdata] = useSearchParams();
  return (
    <>
        <h1> 페이지 6 </h1>
        제목: {bookdata.get("title")}
        <br />
        가격: {bookdata.get("price")}
        <hr />
        
    </>
  )
}

export default Page6