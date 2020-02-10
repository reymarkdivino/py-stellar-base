from typing import Union, TypeVar, List, AsyncGenerator, Generator

from ..call_builder.base_call_builder import BaseCallBuilder
from ..client.base_async_client import BaseAsyncClient
from ..client.base_sync_client import BaseSyncClient
from ..response.transaction_response import TransactionResponse
from ..response.wrapped_response import WrappedResponse

T = TypeVar("T")


class TransactionsCallBuilder(BaseCallBuilder[T]):
    """ Creates a new :class:`TransactionsCallBuilder` pointed to server defined by horizon_url.
    Do not create this object directly, use :func:`stellar_sdk.server.Server.transactions`.

    See `All Transactions <https://www.stellar.org/developers/horizon/reference/endpoints/transactions-all.html>`_

    :param horizon_url: Horizon server URL.
    :param client: The client instance used to send request.
    """

    def __init__(
        self, horizon_url: str, client: Union[BaseAsyncClient, BaseSyncClient]
    ) -> None:
        super().__init__(horizon_url, client)
        self.endpoint: str = "transactions"

    def transaction(
        self, transaction_hash: str
    ) -> "TransactionsCallBuilder[TransactionResponse]":
        """The transaction details endpoint provides information on a single transaction.
        The transaction hash provided in the hash argument specifies which transaction to load.

        See `Transaction Details <https://www.stellar.org/developers/horizon/reference/endpoints/transactions-single.html>`_


        :param transaction_hash: transaction hash
        :return: current TransactionsCallBuilder instance
        """
        self.endpoint = "transactions/{transaction_hash}".format(
            transaction_hash=transaction_hash
        )
        return self

    def for_account(self, account_id: str) -> "TransactionsCallBuilder[T]":
        """This endpoint represents all transactions that affected a given account.

        See `Transactions for Account <https://www.stellar.org/developers/horizon/reference/endpoints/transactions-for-account.html>`_

        :param account_id: account id
        :return: current TransactionsCallBuilder instance
        """
        self.endpoint = "accounts/{account_id}/transactions".format(
            account_id=account_id
        )
        return self

    def for_ledger(self, sequence: Union[str, int]) -> "TransactionsCallBuilder[T]":
        """This endpoint represents all transactions in a given ledger.

        See `Transactions for Ledger <https://www.stellar.org/developers/horizon/reference/endpoints/transactions-for-ledger.html>`_

        :param sequence: ledger sequence
        :return: current TransactionsCallBuilder instance
        """
        self.endpoint = "ledgers/{sequence}/transactions".format(sequence=sequence)
        return self

    def include_failed(self, include_failed: bool) -> "TransactionsCallBuilder[T]":
        """Adds a parameter defining whether to include failed transactions. By default only
        transactions of successful transactions are returned.

        :param include_failed: Set to `True` to include failed transactions.
        :return: current TransactionsCallBuilder instance
        """
        self._add_query_param("include_failed", include_failed)
        return self

    def _parse_response(
        self, raw_data: dict
    ) -> Union[List[TransactionResponse], TransactionResponse]:
        if self._check_pageable(raw_data):
            parsed = [
                TransactionResponse.parse_obj(record)
                for record in raw_data["_embedded"]["records"]
            ]
        else:
            parsed = TransactionResponse.parse_obj(raw_data)
        return parsed

    def stream(
        self
    ) -> Union[
        AsyncGenerator[WrappedResponse[TransactionResponse], None],
        Generator[WrappedResponse[TransactionResponse], None, None],
    ]:
        return self._stream()
