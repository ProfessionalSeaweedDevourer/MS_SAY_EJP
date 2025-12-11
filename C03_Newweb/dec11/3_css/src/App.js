import './App.css';
import CustomCSS1 from './CustomCSS/CustomCSS1';
import CustomCSS2 from './CustomCSS/CustomCSS2';

// 폰트 크기를 동적으로 설정할 변수
const dynamicFontSize = "6vw";
// view width에 따라 동적 반영 => 화면 크기 조절에 따라 폰트 크기가 반응.
// 이것은 css가 아니라 main에서 이렇게 띄우지 않으면 안 됨.

function App() {
  return (
    <>
      <CustomCSS1 />
      <CustomCSS2 c="green" bgc="black" w="200px" h="200px" fs={dynamicFontSize}/>
    </>
  );
}

export default App;
