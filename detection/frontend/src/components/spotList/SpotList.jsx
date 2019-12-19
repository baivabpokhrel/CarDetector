import React from 'react';
import { List, Text } from 'grommet'

const sortSpots = (openSpotsList, takenSpotsList) => {
  const sortedSpots = [];
  for (let i = 0; i < openSpotsList.length; i++) {
    sortedSpots.push({ spotNumber: openSpotsList[i], status: 'Available', })
  }
  for (let i = 0; i < takenSpotsList.length; i++) {
    sortedSpots.push({ spotNumber: takenSpotsList[i], status: 'Taken' })
  }
  return sortedSpots.sort((a, b) => a.spotNumber - b.spotNumber)
}

const ListItem = ({ item }) => {
  return (
    <li>
      <Text bold color="#d65a31">
        Spot {item.spotNumber}
      </Text>
      <span>
        -
     </span>
      <Text bold color={item.status === 'Available' ? '#4CAF50' : '#D32F2F'}>
        {item.status}
      </Text>
    </li>

  )
}
const SpotList = ({ openSpotsList, takenSpotsList }) => {
  console.log(openSpotsList, takenSpotsList)
  if (!openSpotsList || !takenSpotsList) {
    return (
      <div className="text">
        <div className="text-line"> </div>
        <div className="text-line"></div>
        <div className="text-line"></div>
        <div className="text-line"></div>
      </div>
    )
  }
  const sortedSpots = sortSpots(openSpotsList, takenSpotsList)
  return (
    <div style={{ height: '20vh', overflowY: 'scroll' }}>
      <List
        primaryKey="spotNumber"
        secondaryKey="status"
        data={sortedSpots}
        children={(item, index) => {
          return (<ListItem item={item} />)
        }}
      />
    </div>
  )
}

export default SpotList
