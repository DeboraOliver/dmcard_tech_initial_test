import React, { Component, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import NewCardForm from "./NewCardForm";

class NewCardModal extends Component {
  state = {
    modal: false
  };

  toggle = () => {
    this.setState(previous => ({
      modal: !previous.modal
    }));
  };

  render() {
    const create = this.props.create;

    var title = "Editando seu Pedido";
    var button = <Button onClick={this.toggle}>Edite</Button>;
    if (create) {
      title = "Solicite seu Cartão";

      button = (
        <Button
          color="primary"
          className="float-right"
          onClick={this.toggle}
          style={{ minWidth: "200px" }}
        >
          Novo Cartão
        </Button>
      );
    }

    return (
      <Fragment>
        {button}
        <Modal isOpen={this.state.modal} toggle={this.toggle}>
          <ModalHeader toggle={this.toggle}>{title}</ModalHeader>

          <ModalBody>
            <NewCardForm
              resetState={this.props.resetState}
              toggle={this.toggle}
              cartao={this.props.cartao}
            />
          </ModalBody>
        </Modal>
      </Fragment>
    );
  }
}

export default NewCardModal;