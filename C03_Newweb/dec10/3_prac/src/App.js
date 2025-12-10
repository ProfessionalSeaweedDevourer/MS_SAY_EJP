import './App.css';
import Clicker from './clicker';

function App() {
  return (
    <>
      <Clicker />
      <hr />
      <Clicker />
    </>
  );
}

export default App;

// 개발이 끝나면 프로젝트 폴더에서 yarn build 수행.
// /build 디렉토리: 단독 실행 불가능하지만 이 내용물을 서버 컴퓨터에 넣어서 띄우면 돌아감
// 빌드를 건너뛰고 전부 옮기는 것은 파일도 너무 많고 뻘짓