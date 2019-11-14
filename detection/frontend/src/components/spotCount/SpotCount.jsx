import React from 'react';
import styled from '@emotion/styled'
const Counter = styled('h2')`
font-size: 35px;
color: blue;
`
const SpotCount  = ({count}) => {
  return(
    <div>
    <h1>Spots</h1>
    <Counter>{count}</Counter>
    </div>
  )
}

export default SpotCount;
