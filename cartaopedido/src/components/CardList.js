import React, { Component } from "react";
import { Table } from "reactstrap";
import NewCardModal from "./NewCardModal";

import ConfirmRemovalModal from "./ConfirmRemovalModal";

class CardList extends Component {
  render() {
    const cards = this.props.cards;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>Nome</th>
            <th>Email</th>
            <th>Renda</th>
            <th>Pedido em</th>
			<th>Pontuação</th>
			<th>Aprovação</th>
			<th>Crédito</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {!cards || cards.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, no one here yet</b>
              </td>
            </tr>
          ) : (
            cards.map(card => (
              <tr key={card.pk}>
                <td>{card.nome}</td>
                <td>{card.email}</td>
                <td>{card.renda}</td>
                <td>{card.pedido_em}</td>
				<td>{card.pontuacao}</td>
				<td>{card.aprovacao}</td>
				<td>{card.credito}</td>
                <td align="center">
                  <NewCardModal
                    create={false}
                    card={card}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmRemovalModal
                    pk={card.pk}
                    resetState={this.props.resetState}
                  />
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default CardList;