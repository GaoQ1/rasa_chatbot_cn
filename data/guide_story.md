
## Generated Story No1
* greet
    - utter_greet
* request_management{"package": "套餐"}
    - slot{"package": "套餐"}
    - utter_ask_package
* inform_package{"package": "套餐一"}
    - slot{"package": "套餐一"}
    - utter_ack_management
    - utter_ask_morehelp
* request_search{"item": "话费"}
    - slot{"item": "话费"}
    - utter_ask_phonenum
* inform_current_phone{"phone_number": "18912936976"}
    - slot{"phone_number": "18912936976"}
    - utter_ask_time
* inform_time{"time": "三月"}
    - slot{"time": "三月"}
    - action_search_consume
* request_search{"item": "流量"}
    - slot{"item": "流量"}
    - utter_ask_time
* inform_time{"time": "四月"}
    - slot{"time": "四月"}
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_goodbye
    - action_restart

