import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { Meter, Box, Text, Stack } from 'grommet'
const SpotCount = ({ availableSpots, totalSpots }) => {
  const [active, setActive] = useState();
  const [label, setLabel] = useState();
  return (
    <div>
      <Box align="center" pad="large">
        <Stack anchor="center">
          <Meter
            type="circle"
            background="#393e46"
            values={[
              {
                color: "#d65a31",
                value: totalSpots - availableSpots,
                onHover: over => {
                  setActive(over ? totalSpots - availableSpots : 0);
                  setLabel(over ? "Spots In Use" : undefined);
                }
              },


            ]}
            max={totalSpots}
            size="small"
            thickness="medium"
          />
          <Box align="center">
            <Box direction="row" align="center" pad={{ bottom: "xsmall" }}>
              <Text color="#d65a31" size="xxlarge" weight="bold">
                {active || availableSpots}
              </Text>
            </Box>
            <Text bold color="#eeeeee">{label || "Spots Available"}</Text>
          </Box>
        </Stack>
      </Box>
    </div>
  )
}

SpotCount.propTypes = {
  availableSpots: PropTypes.number,
  totalSpots: PropTypes.number

}
export default SpotCount;
