program pippo
  use HDF5
  implicit none
  integer, parameter :: bufsize = 1000000
  integer(hid_t) :: file_id, &
                    dataset_id,dataspace_id,datatype_id,prop_id
  integer :: rank 
  integer(HSIZE_T),dimension(1) :: dims,maxdims,offset
  INTEGER(HID_T) :: filespace_id,memspace_id
  integer :: data(bufsize)
  integer :: error,i,j

  rank = 1
  dims(1) = 100000000




  do i=1,100000000/bufsize
    call h5open_f(error)
    call h5fopen_f("ciao.h5", H5F_ACC_RDONLY_F, file_id, error)
    call h5dopen_f(file_id,'test',dataset_id,error)
    CALL h5dget_space_f(dataset_id, filespace_id, error)
    dims(1) = bufsize
    offset = (i-1)*bufsize
    print *, "i = ",i,"/",100000000/bufsize
    CALL h5sselect_hyperslab_f(filespace_id, H5S_SELECT_SET_F, &
                               offset, dims, error)

    CALL h5screate_simple_f(RANK, dims, memspace_id, error)

    CALL H5Dread_f(dataset_id, H5T_NATIVE_INTEGER, data, dims, error, &
                      mem_space_id=memspace_id, file_space_id=filespace_id)
    print *, data(1)
    call h5sclose_f(memspace_id,error)
    call h5dclose_f(dataset_id,error)
    call h5fclose_f(file_id,error)
    call h5close_f(file_id)
  enddo

! call h5tclose_f(datatype_id,error)
! call h5sclose_f(dataspace_id,error)
  
end



