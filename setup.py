import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

current_version = str('1.1.0')

setuptools.setup(
    name='structlog-sentry-lambda',

    version=current_version,
    description='An AWS approved version of https://github.com/TeoZosa/structlog-sentry-logger '
                'which is compatible to AWS Lambda as well as AWS Fargate',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Rungutan/structlog-sentry-lambda',
    download_url='https://github.com/Rungutan/structlog-sentry-lambda/archive/{}.tar.gz'.format(current_version),

    author='Rungutan',

    author_email='support@rungutan.com',

    project_urls={
        'Bug Reports': 'https://github.com/Rungutan/structlog-sentry-lambda/issues',
        'Source': 'https://github.com/Rungutan/structlog-sentry-lambda/',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[  # Optional
        # How mature is this project?
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Audience
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',

        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing :: Acceptance',
        'Topic :: Software Development :: Testing :: BDD',
        'Topic :: Software Development :: Testing :: Mocking',
        'Topic :: Software Development :: Testing :: Traffic Generation',
        'Topic :: Software Development :: Testing :: Unit',

        # License
        'License :: OSI Approved :: MIT License',

        # Supported Python versions
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],

    keywords='rungutan rungutan-cli rungutan_cli cli load testing load-testing load_testing stress'
             'stress-testing stress_testing api api-testing api_testing api_load_testing api-load-testing'
             'api_stress_testing api-stress-testing performance performance-testing performance_testing'
             'api-performance-testing api_performance_testing serverless workflow-testing workflow_testing',
    python_requires='>=3.6',
    install_requires=['sentry-sdk', 'colorama', 'python-dotenv', 'structlog', 'orjson', 'rich'],
    extras_require={
        'test': ['coverage'],
    }
)
