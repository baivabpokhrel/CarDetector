import React, {useState} from 'react';
import './App.css';
import { SpotCount } from './components';

const App = () =>  {
  const [count, setCount] = useState(0);
  return (
    <div className="App">
      <header className="App-header">
        <h1>Parking Spot Detector</h1>
      </header>
      <div>
        <button onClick={() => setCount(count+1)}>+</button>
          <button onClick={() => setCount(count-1)}>-</button>

        <SpotCount count={count}/>
      </div>
    </div>
  );
}

export default App;
