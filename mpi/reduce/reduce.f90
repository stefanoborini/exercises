program ex1
    use mpi
    implicit none
    integer :: err, comm,rank, siz
    integer :: info = -1
    integer :: total = -1
    integer :: all_total = -1
    integer :: info_array(2) = -1
    integer :: total_array(2) = -1

    call mpi_init(err)
    call mpi_comm_rank(MPI_COMM_WORLD, rank, err)
    call mpi_comm_size(MPI_COMM_WORLD, siz, err)

    info = rank*10

    call MPI_Barrier(MPI_COMM_WORLD, err)

    call MPI_Reduce(info, total, 1, MPI_INTEGER, MPI_SUM, root=0, comm=MPI_COMM_WORLD, ierror=err)
   
    print *, "rank = ", rank, "total = ", total
    call MPI_Barrier(MPI_COMM_WORLD, err)

    call MPI_AllReduce(info, all_total, 1, MPI_INTEGER, MPI_SUM, comm=MPI_COMM_WORLD, ierror=err)
    print *, "rank = ", rank, "all total = ", all_total

    info_array(1) = rank*10
    info_array(2) = rank*100

    call MPI_Barrier(MPI_COMM_WORLD, err)

    call MPI_Reduce(info_array, total_array, 2, MPI_INTEGER, MPI_SUM, root=0, comm=MPI_COMM_WORLD, ierror=err)

    if (rank == 0) then
        print *, "total_array", total_array
    endif

    call mpi_finalize(err)
end program
