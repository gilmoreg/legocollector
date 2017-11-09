import styled from 'styled-components';

export const StyledWatchHeader = styled.div`
  max-width: 760px;
  background-color: rgba(255,246,229,0.7);
  border-bottom: none;
  border-radius: 5px 5px 0px 0px;
  margin: 0 auto;
  display: flex;
  justify-content: space-around;
  z-index: -2;
`;

export const StyledThumbnail = styled.div`
  flex: 0 0 20%;
  align-self: center;
  padding: 5px;
  padding-top: 10px;
`;

export const StyledTitle = styled.div`
  flex: 0 0 50%;
  align-self: center;
  text-align: left;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;

  @media (min-width: 640px) {
    font-size: 24px;
  }
`;

export const StyledStock = styled.div`
  flex: 0 0 20%;
  color: green;
  align-self: center;
  font-size: 36px;
  padding-top: 5px;

  @media (min-width: 640px) {
    font-size: 60px;
  }
`;

export const StyledStockP = styled.p`
  margin-top: 5px;
  margin-bottom: 5px;
  font-size: 14px;
  color: black;

  @media (min-width: 640px) {
    font-size: 24px;
  }
`;

export const StyledImg = styled.img`
  width: 100%;
`;
