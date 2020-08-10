## [0.0.39] - 2020-08-10
- Update alert path for tsanaclient.

## [0.0.38] - 2020-08-10
- Do not list blob when download model as it will take too much time.

## [0.0.37] - 2020-08-07
- Update alert schema, add start time, end time and gran to request body.
- Add trainable field for plugin service, do not need training when trainable is false.

## [0.0.36] - 2020-08-06
- Add push alert api(Zhao Ming).
  
## [0.0.35] - 2020-08-05
- Update alert schema.

## [0.0.34] - 2020-08-03
- Fix meta deserialize issue caused by str when storage meta, such as " to ' and 'true' to 'True'.

## [0.0.33] - 2020-08-03
- Fix null state issue for clear_state_when_necessary.

## [0.0.32] - 2020-08-03
- Fix date time json serialize issue for trigger_alert.

## [0.0.31] - 2020-07-31
- Change get_inference_time_range to get_inference_time_list as it may cause confusion.

## [0.0.30] - 2020-07-31
- Add trigger alert api.

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