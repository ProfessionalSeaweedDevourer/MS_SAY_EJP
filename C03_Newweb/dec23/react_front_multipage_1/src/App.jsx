import { Routes, Route, Navigate, } from "react-router-dom"
import { Link } from "react-router-dom"
import Page1 from "./Pages/Page1"
import Page2 from "./Pages/Page2"
import Page3 from "./Pages/Page3"
import Page4 from "./Pages/Page4"
import Page5 from "./Pages/Page5"
import Page6 from "./Pages/Page6"

function App() {

  // index는 Route index element= 꼴로도 구현 가능.
  // 첫 페이지는 path="/" 내지 index, 나머지로 들어오는 것(*)을 보안을 위해 처리
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/p1.go" replace />} />
      <Route path="/p1.go" element={<Page1 />} />
      <Route path="/p2.go" element={<Page2 />} />
      <Route path="/p3.go" element={<Page3 />} />
      <Route path="/p4.go/:name/:age" element={<Page4 />} />
      <Route path="/p5.go/:name/:price" element={<Page5 />} />
      <Route path="/p6.go/:title/:price" element={<Page6 />} />
      <Route path="/p7.go" element={<Page7 />} />
      <Route path="/p8.go" element={<Page8 />} />
      <Route path="*" element={<Page9 />} />
    </Routes>
  )
}

export default App
