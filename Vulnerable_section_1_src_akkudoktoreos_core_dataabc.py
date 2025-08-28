                     # We jump back by 1 hour
                     # Repeat the value(s) (reuse value index)
                     for i in range(interval_steps_per_hour):
                        logger.debug(f"{i+1}: Repeat at {next_time} with index {value_index}")
                         timestamps_with_indices.append((next_time, value_index))
                         next_time = next_time.add(seconds=interval.total_seconds())
                 else:
                     # We jump forward by 1 hour
                     # Drop the value(s)
                     logger.debug(
                        f"{i+1}: Skip {interval_steps_per_hour} at {next_time} with index {value_index}"
                     )
                     value_index += interval_steps_per_hour
 