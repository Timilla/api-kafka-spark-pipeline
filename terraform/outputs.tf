################################################################################
# Client Machine (EC2 instance)
################################################################################
output "execute_this_to_access_the_bastion_host" {
  value = "ssh ec2-user@${aws_instance.bastion_host.public_ip} -i cert.pem"
}


################################################################################
# Spark
################################################################################

output "spark_arn" {
  description = "Amazon Resource Name (ARN) of the application"
  value       = module.emr_serverless_spark.arn
}

output "spark_id" {
  description = "ID of the application"
  value       = module.emr_serverless_spark.id
}

#output "spark_security_group_arn" {
#  description = "Amazon Resource Name (ARN) of the security group"
#  value       = module.emr_serverless_spark.security_group_arn
#}

#output "spark_security_group_id" {
#  description = "ID of the security group"
#  value       = module.emr_serverless_spark.security_group_id
#}