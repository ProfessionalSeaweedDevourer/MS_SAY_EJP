import React from 'react'
import { useState } from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'

// 여기에서 데이터를 등록하고 이를 P3에서 로드

const Page2 = () => {

  const [product, setProduct] = useState({name:"", price:""})

  const changeProduct = (e) => {
    setProduct({ ...product, [e.target.name]: e.target.value })
  }

  const regProduct = () => {
    axios
      .get(
        `http://localhost:9999/product.reg?name=${product.name}&price=${product.price}`
      )
      .then((res) => {
        sessionStorage.setItem("productInfo", res.data.token)
      })

    alert(JSON.stringify(product))
  }

  return (
    <>
      <h1> 페이지 2 </h1>

      제품명: {" "}<input value={product.name} name="name" onChange={changeProduct}/>
      <br />
      가격: {" "}<input value={product.price} name="price" onChange={changeProduct} />
      <br />
      <button onClick={regProduct}> 등록 </button>
      <hr />

      <a href="/p3.go"> 페이지 3로 이동하기(a 태그 사용) </a>
      <br />
      <Link to="/p3.go"> 페이지 3로 이동하기(Link to 사용) </Link>
    </>
  )
}

export default Page2