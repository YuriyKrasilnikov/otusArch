import React, {useEffect} from 'react';
import logo from './logo.svg';
import './App.css';

import { client, helloRequest, helloStream } from './grpc-client'

const App = ( ) => {

  useEffect(() => {
    setInterval(()=>{
      for (let i = 0; i < 50; i++) {
        helloRequest();
      }
    }, 3000);

    helloStream();
  });

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="LearnReact/"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React and Kuber
        </a>
      </header>
    </div>
  );
}

export default App;
