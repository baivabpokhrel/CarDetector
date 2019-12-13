import React from 'react';
import PropTypes from 'prop-types';
import styled from '@emotion/styled'
const Counter = styled('h2')`
font-size: 35px;
color: blue;
`
const SpotCount = ({ availableSpots, totalSpots }) => {
  return (
    <div>
      <h1>Available Spots</h1>
      <Counter>{availableSpots} / {totalSpots} </Counter>
    </div>
  )
}

SpotCount.propTypes = {
  availableSpots: PropTypes.number,
  totalSpots: PropTypes.number

}
export default SpotCount;
