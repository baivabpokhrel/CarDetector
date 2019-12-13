import React, { useState } from 'react';

const Image = ({ srcBefore, srcAfter, ...props }) => {
  const [visibleImage, setVisibleImage] = useState(false)

  return (
    <img src={visibleImage ? srcBefore : srcAfter} {...props} onClick={() => setVisibleImage(!visibleImage)} alt={visibleImage ? "Parking Lot image" : "Parking lot image with overlay"} />
  )
}

export default Image;
