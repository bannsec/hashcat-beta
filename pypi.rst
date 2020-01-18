hashcat-beta
============

.. note::

    This project is not in any way officially endorsed by the hashcat team.

This project is my attempt to make installing and using hashcat easier. Specifically, it solves the following:

* No need to browse to hashcat and download
* No need to download all the separate processors (see their github)
* The tools are automatically in your path, no need to cd into hashcat directory

   * hashcat doesn't officially support running it from a separate directory. this library has it's own fix built in to allow this.

* Easy to update or fully remove

Install
-------

.. code-block:: bash

    $ pip install hashcat-beta

Running
-------

Run it as if you were running hashcat normally. It exposes multiple utilities as well.

.. code-block:: bash

    $ hashcat -h
    $ pp64 -h
    $ cap2hccapx -h
    $ kwp -h

CLI Menu
~~~~~~~~

For a cli menu to hashcat, see https://pypi.org/project/hashcrack/
