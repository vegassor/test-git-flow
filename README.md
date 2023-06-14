## Tasks
- Create helm chart that deploys all services
- Create and configure 5 staging namespaces
    * Restrict in cluster networking outside of the namespace
    * Configure DSAS users (on master DSAS) to sync with
- Create process of making lightweight dumps
    * Create scripts to make dumps (dts, rtbm?)
    * Create S3 bucket and roles for downloading dumps
- Create GitHub Actions workflow to deploy environment
    * Start it on push to master when one of environment files is changed

## Steps to deploy a new environment
1. Read values, get enabled services
2. Get latest images, where images are not specified
3. Download rtbm, dts dumps 
   * from S3?
4. Deploy auxilary services:
    * one PostgreSQL instance, many databases: dts, dsas, rtbmedia
    * clickhouse-storage
    * one Vault
5. Deploy helm chart, set latest values to enabled services that have not specified images
6. Sync DSAS with master
