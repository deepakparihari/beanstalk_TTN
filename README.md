# beanstalk_TTN
automation 
[Elastic Beanstalk Environment]
        |
        v
[Application Load Balancer (ALB)]
        |
        v
[CloudWatch Logs/ALB Metrics]
        |
        v
[CloudWatch Alarm on 4xx Error Threshold]
        |
        v
[AWS SNS Topic or Direct Target]
        |
        v
[AWS Lambda Function]
        |
        v
[Elastic Beanstalk Environment Restart API]
