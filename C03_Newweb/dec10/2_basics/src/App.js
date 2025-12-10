import logo from './logo.svg';
import './App.css';

// React: Meta에서 만든 JS OOP 라이브러리.
// Virtual DOM 개념 활용: 소스가 바로 화면에 그려지지 않고, 중간에 가상 VDOM을 한 번 거침
//  > 소스 변화가 일어나면 VDOM에 다시 그리고, 실제 화면과 달라진 부분'만' 화면에 반영
//  > 동적인 사이트 구축에 있어 유리.
//    > 대신 정적인 사이트에서는 괜히 자원만 많이 먹고 느림

// public/index.html -> <div id="root"></div>
// src/index.js : 기본 설정 & index.html의 root 영역에 App.js 구현
// src/App.js : 실제 작업이 이루어지는 곳

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
