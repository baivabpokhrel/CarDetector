import React, { useState } from 'react';

const Image = ({ srcBefore, srcAfter, ...props }) => {
  const [visibleImage, setVisibleImage] = useState(false)

  return (
    <img src={visibleImage ? srcBefore : srcAfter} {...props} onClick={() => setVisibleImage(!visibleImage)} />
  )
}

export default Image;
