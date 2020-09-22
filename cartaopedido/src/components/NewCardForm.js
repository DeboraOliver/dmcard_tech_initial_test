import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class NewCardForm extends React.Component {
  state = {
    pk: 0,
    name: "",
    email: "",
    renda: ""
  };

  componentDidMount() {
    if (this.props.card) {
      const { pk, nome, renda, email} = this.props.card;
      this.setState({ pk, nome, renda, email});
    }
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  createcard = e => {
    e.preventDefault();
    axios.post(API_URL, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  editcard = e => {
    e.preventDefault();
    axios.put(API_URL + this.state.pk, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.props.card ? this.editCard : this.createCard}>
        <FormGroup>
          <Label for="nome">Nome:</Label>
          <Input
            type="text"
            name="nome"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.nome)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="email">Email:</Label>
          <Input
            type="email"
            name="email"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.email)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="renda">Renda:</Label>
          <Input
            type="text"
            name="renda"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.renda)}
          />        
        </FormGroup>
        <Button>Enviar</Button>
      </Form>
    );
  }
}

export default NewCardForm;