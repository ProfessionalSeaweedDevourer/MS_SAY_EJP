import React from 'react'
// import d3mc from "./Design3.module.css"
import { useEffect } from 'react'

const Design3 = () => {

    useEffect(() => {
        const h = 180
        const w = 80

        alert('키 ${h}cm / 몸무게 ${w}kg')

        return () => {}
    }, [])

  return (
    <div className=''>Design3</div>
  )
}

export default Design3