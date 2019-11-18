import React, { useState } from 'react';
import { SpotCount } from '../../components';

const HomeView = ({}) => {
  const [count, setCount] = useState(0);
  return (
    <div>
      Home
      <div>
        <button onClick={() => setCount(count + 1)}>+</button>
        <button onClick={() => setCount(count - 1)}>-</button>

        <SpotCount count={count} />
      </div>
    </div>
  );
};

export default HomeView;
