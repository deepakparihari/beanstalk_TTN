# beanstalk_TTN
Architecture Flow: Auto-Restart Elastic Beanstalk on 4xx Errors

automation Steps : 


[Elastic Beanstalk Environment]
        |
        
[Application Load Balancer (ALB)]
        |

[CloudWatch Logs/ALB Metrics]
        |

[CloudWatch Alarm on 4xx Error Threshold]
        |

[AWS SNS Topic or Direct Target]
        |

[AWS Lambda Function]
        |

[Elastic Beanstalk Environment Restart API]
