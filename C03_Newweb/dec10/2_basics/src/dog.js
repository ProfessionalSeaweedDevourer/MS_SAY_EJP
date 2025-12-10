import React, {useState} from 'react'

const Dog = () => {
    const [name, setName] = useState("???")
    const [age, setAge] = useState(0);
  return (
    <>
        <h1> {name} </h1>
        <h1> {age} </h1>
        이름: <input value={name} onChaWWnge={(e) => { setName(e.target.value);}}/> <br />
        나이: <input value={age} onChange={setAge} /> <br />
        <button>출력</button>
    </>
  )
}

export default Dog