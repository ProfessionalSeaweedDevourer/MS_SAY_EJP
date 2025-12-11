import React, {useState} from 'react'

const Rptstmt3 = () => {
    const [snacks, setSnacks] = useState([
        {name:"빼빼로", price:2000, color:"brown"},
        {name:"새콤달콤", price:500, color:"pink"},
        {name:"쌀로별", price:3000, color:"yellow"},
    ])

    const snackTrs = snacks.map((s,i)=>{
        return (
            <tr style={{color:s.color}}>
                <td>
                    {s.name}
                </td>
                <td>
                    {s.price}
                </td>
            </tr>
        )
    })

  return (
    <table border={1}>
        <tr><td>제품명</td><td>가격</td></tr>
        {snackTrs}
    </table>
  )
}

export default Rptstmt3