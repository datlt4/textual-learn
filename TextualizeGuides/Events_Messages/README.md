# [Events and Messages](https://textual.textualize.io/guide/events/)

## Messages

- Events are a particular kind of message sent by Textual in response to input and other state changes.

- Events are reserved for use by Textual, but you can also create custom messages for the purpose of coordinating between widgets in your app.

- More on that later, but for now keep in mind that events are also messages, and anything that is true of messages is true of events.

## Message Queue

- Every `App` and `Widget` object contains a `message queue`. You can think of a `message queue` as orders at a restaurant. The chef takes an order and makes the dish. Orders that arrive while the chef is cooking are placed in a line. When the chef has finished a dish they pick up the next order in the line.
