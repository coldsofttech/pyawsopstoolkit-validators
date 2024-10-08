# pyawsopstoolkit_validators

The **pyawsopstoolkit_validators** package provides a comprehensive set of validation classes specifically crafted for
use with AWS (Amazon Web Services). These validators are meticulously designed to cater to the unique requirements
within the AWS ecosystem, covering a wide array of aspects such as AWS Resource Names (ARNs), Policy Statements, and
more. By leveraging these validators, developers can ensure that their AWS-related inputs and configurations adhere to
the necessary standards and formats, thereby enhancing the reliability and security of their applications deployed on
AWS.

## Getting Started

Ready to supercharge your AWS operations? Let's get started with **pyawsopstoolkit_validators!**

### Installation

Install **pyawsopstoolkit_validators** via pip:

```bash
pip install pyawsopstoolkit_validators
```

## Documentation

### account_validator

The **account_validator** package provides methods to validate AWS account information, ensuring accuracy and
consistency in account details. It includes constants and methods for validating account numbers.

#### Constants

- `NUMBER_PATTERN`: Regular expression pattern for validating account numbers. The pattern ensures that the account
  number consists of exactly 12 digits.

#### Methods

- `number(value: str, raise_error: Optional[bool] = True, custom_error_message: Optional[str] = None) -> bool`:
  Validates if the given AWS account number is valid.

#### Usage

```python
from pyawsopstoolkit_validators.account_validator import number

# Validate account numbers
print(number('123456789012'))  # Output: True
print(number('123'))  # Output: False
```

#### References

- [AWS Documentation: DescribeAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeAccount.html)

### arn_validator

The **arn_validator** package validates AWS ARNs (Amazon Resource Names) according to the AWS ARN format. This package
provides methods to validate various aspects of ARNs, including the partition, service, region, account ID, and resource
ID.

#### Constants

- `ARN_PATTERN`: Regular expression pattern for AWS ARNs.

#### Methods

- `arn(value: Union[str, list], raise_error: Optional[bool] = True, custom_error_message: Optional[str] = None) -> bool`:
  Validates if the given ARN(s) match the ARN pattern.

#### Usage

```python
from pyawsopstoolkit_validators.arn_validator import arn

# Validate ARNs
print(arn('arn:aws:ec2:us-east-1:123456789012:vpc/vpc-0e9801d129EXAMPLE', False))  # Output: True
print(arn('arn::iam:us-east-1:123456789012:user', False))  # Output: False
```

#### References

- [AWS Documentation: ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html)

### policy_validator

The **policy_validator** package validates AWS IAM policy documents. This package provides methods to validate various
aspects of IAM policies, ensuring their correctness and compliance.

#### Constants

- `VERSION_PATTERN`: Regular expression pattern for validating version strings in policies.
- `EFFECT_PATTERN`: Regular expression pattern for validating effect strings in policies.
- `PRINCIPAL_PATTERN`: Regular expression pattern for validating principal strings in policies.

#### Methods

- `policy(value: dict, raise_error: Optional[bool] = True, custom_error_message: Optional[str] = None) -> bool`:
  Validates if the given policy dictionary is valid.

#### Usage

```python
from pyawsopstoolkit_validators.policy_validator import policy

# Validate IAM policy documents
print(policy(
    {
        "Version": "2012-10-17",
        "Id": "1",
        "Statement": {
            "Sid": "1",
            "Principal": "*",
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*",
            "Condition": {
                "Bool": {
                    "aws:SecureTransport": "true"
                }
            }
        }
    }, False
))  # Output: True
print(policy(
    {
        "Version": "2012-10-17",
        "Id": "1"
    }, False
))  # Output: False
```

#### References

- [AWS Documentation: IAM Policy Grammar](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_grammar.html)

### region_validator

The **region_validator** packages validates AWS regions. This package provides methods to validate various aspects of
AWS, such as region code.

#### Constants

- `REGION_PATTERN`: Regular expression pattern used to validate region codes.

#### Methods

- `region(value: str, raise_error: Optional[bool] = True, custom_error_message: Optional[str] = None) -> bool`:
  Validates if the given region code is valid.

#### Usage

```python
from pyawsopstoolkit_validators.region_validator import region

# Validate region codes
print(region('eu-west-1', False))  # Output: True
print(region('Ohio', False))  # Output: False
```

#### References

- [AWS Documentation: DescribeAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeAccount.html)

# License

Please refer to the [MIT License](LICENSE) within the project for more information.

# Contributing

We welcome contributions from the community! Whether you have ideas for new features, bug fixes, or enhancements, feel
free to open an issue or submit a pull request on [GitHub](https://github.com/coldsofttech/pyawsopstoolkit-validators).