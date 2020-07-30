## [0.0.29] - 2020-07-29
- Compare params and series set with different order.
- Set owner for model and set state to fail if owner is dead.

## [0.0.28] - 2020-07-28
- Handle empty row key in azure table.
- Use modelId in request body only when it's not empty.

## [0.0.27] - 2020-07-27
- Fix meta logging bug when state, context or last_error is None.
- Use modelId in parameters if exists.
- Use context in do_verify, do_train, do_inference.
- Add app_init to replace adding restful apis by users.
- Refine model file management.