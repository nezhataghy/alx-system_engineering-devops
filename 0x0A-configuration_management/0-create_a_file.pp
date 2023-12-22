# Creating a file using puppet
file { 'school':
    path    => '/tmp/school',
    content => 'I love Puppet',
    group   => 'www-data',
    mode    => '0744',
    owner   => 'www-data',
}
