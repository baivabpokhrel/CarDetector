import React from 'react';
import PropTypes from 'prop-types';
const Selector = ({ lots, onClick }) => {
  return (
    <div>

      <select>
        {lots.map(lot =>
          <option value={lot.id}>{lot.name}</option>
        )}
      </select>


    </div>
  )
}

Selector.propTypes = {
  lots: PropTypes.arrayOf(
    PropTypes.shape(
      {
        name: PropTypes.string,
        id: PropTypes.string
      }
    )
  )
}
export default Selector;
