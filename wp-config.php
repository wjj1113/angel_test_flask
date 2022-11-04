<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

/**
 * Database connection information is automatically provided.
 * There is no need to set or change the following database configuration
 * values:
 *   DB_HOST
 *   DB_NAME
 *   DB_USER
 *   DB_PASSWORD
 *   DB_CHARSET
 *   DB_COLLATE
 */

/**
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */

define('AUTH_KEY',         ';U(bj9-(}?@Ev:<Ut>4-:ud,49%.Atw_Y!JyXVR6dZ7,k=Q|ve;g[<hkUaxudy:=');
define('SECURE_AUTH_KEY',  'WRcFsNYzPBQDFX5nFwKNk<F]Xd?aSk^EaP-59O(8d2?txp0H6cnAp~Dgf<LSc^N~');
define('LOGGED_IN_KEY',    'T[e)NkWg{p[{z!H-GTL!+;5>yOwQ(3[VXQzg!Rjd~Swt*!<Lc|C2Q1>|#?kNsjWO');
define('NONCE_KEY',        '].5]x*Ao2gU;9x5vhMv:#!BQJ@?o0=iznySEP.,WO8yuO9%zXBCxJdaCNiHDwh9c');
define('AUTH_SALT',        'QC]]=_t*AA;lOY^Vv_P]ttmcq(5Us7fKD$FFamkSk}_F3A[#5wWVtRTy2.-l|U*S');
define('SECURE_AUTH_SALT', 'RAHQ}+En@[NYNX5mQF0[.-OW:ufrXA{S1+r7ZaA~6wrMImD$b#3k.;x3+K!yU9QC');
define('LOGGED_IN_SALT',   'Lm?1vX1dXnVxOqi+.A[Iz.}2rAPeyA={z^EKKH~8H1Ms0[QSJDS!z(rn.BipK:uh');
define('NONCE_SALT',       'e_O)1UB0%u6+Em$E5>[89cB[fn_?PBU,DrZ#^M%Hw:*n[L#8@;xUb.5mrxSi8*z#');

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
if ( ! defined( 'WP_DEBUG') ) {
	define('WP_DEBUG', false);
}

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
  define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
