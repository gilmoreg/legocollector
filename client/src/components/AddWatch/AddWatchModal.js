/* eslint-disable jsx-a11y/no-static-element-interactions */
import React from 'react';
import PropTypes from 'prop-types';
import Modal from 'react-modal';
import AddWatchModalContent from './AddWatchModalContent';
import './AddWatchModal.css';

Modal.setAppElement("#root");

const AddWatchModal = (props) => (
  <Modal
    isOpen={props.open}
    contentLabel="Add New Watch"
    overlayClassName="Overlay"
    className="AddWatchModal"
    shouldCloseOnOverlayClick
    onRequestClose={props.close}
    role="dialog"
  >
    <AddWatchModalContent
      open={props.open}
      close={props.close}
    /> 
  </Modal>
);

AddWatchModal.defaultProps = {
  open: false,
  close: () => {},
};

AddWatchModal.propTypes = {
  open: PropTypes.bool,
  close: PropTypes.func,
};

export default AddWatchModal;
